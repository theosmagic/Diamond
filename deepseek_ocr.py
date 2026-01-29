#!/usr/bin/env python3
import argparse
import os
import sys
import torch
from transformers import AutoModel, AutoTokenizer
from PIL import Image
import fitz  # PyMuPDF
import io

def pdf_to_images(pdf_path, dpi=144):
    images = []
    pdf_document = fitz.open(pdf_path)
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        img_data = pixmap.tobytes("png")
        img = Image.open(io.BytesIO(img_data)).convert('RGB')
        images.append(img)
    pdf_document.close()
    return images

def run_ocr(input_path, output_dir, model_name='deepseek-ai/DeepSeek-OCR-2', device=None, streaming=True):
    if device is None:
        try:
            if torch.cuda.is_available():
                device = 'cuda'
                torch.cuda.get_device_count()
            else:
                device = 'cpu'
        except Exception as e:
            print(f"CUDA initialization failed: {e}. Falling back to CPU.")
            device = 'cpu'
    
    print(f"Using device: {device}")
    
    print(f"Loading tokenizer: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    
        print(f"Loading model: {model_name}")
        # Use 'eager' for CPU, flash_attention_2 for CUDA if supported
        attn_implementation = 'flash_attention_2' if device == 'cuda' else 'eager'
        
        model = AutoModel.from_pretrained(
            model_name, 
            attn_implementation=attn_implementation, 
            trust_remote_code=True, 
            # use_safetensors=True
        )    
    if device == 'cuda':
        model = model.eval().cuda().to(torch.bfloat16)
    else:
        model = model.eval().to(torch.float32)
    
    # Check if input is PDF or image
    if input_path.lower().endswith('.pdf'):
        print(f"Converting PDF to images: {input_path}")
        images = pdf_to_images(input_path)
    else:
        images = [Image.open(input_path).convert('RGB')]
    
    prompt = "<image>\n<|grounding|>Convert the document to markdown. "
    
    all_results = []
    for i, img in enumerate(images):
        print(f"Running OCR on page/image {i+1}/{len(images)}...")
        
        # We use model.infer which internally uses generate and streamer
        # If we want to force streaming behavior, we ensure eval_mode=False
        # Note: model.infer already has a streamer (NoEOSTextStreamer) if eval_mode=False
        
        temp_image_path = f"temp_page_{i}.png"
        img.save(temp_image_path)
        
        try:
            res = model.infer(
                tokenizer, 
                prompt=prompt, 
                image_file=temp_image_path, 
                output_path=output_dir, 
                base_size=1024, 
                image_size=768, 
                crop_mode=True, 
                save_results=True,
                eval_mode=not streaming
            )
            all_results.append(res)
        finally:
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)
    
    print(f"\nOCR Complete. Results saved to: {output_dir}")
    return all_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DeepSeek-OCR-2 CLI with Streaming')
    parser.add_argument('--input', type=str, required=True, help='Path to image or PDF file')
    parser.add_argument('--output', type=str, default='ocr_results', help='Output directory')
    parser.add_argument('--model', type=str, default='deepseek-ai/DeepSeek-OCR-2', help='Model name or path')
    parser.add_argument('--cpu', action='store_true', help='Force CPU usage')
    parser.add_argument('--no-stream', action='store_false', dest='streaming', help='Disable streaming output')
    
    args = parser.parse_args()
    
    device = 'cpu' if args.cpu else None
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found.")
        sys.exit(1)
        
    os.makedirs(args.output, exist_ok=True)
    
    try:
        run_ocr(args.input, args.output, args.model, device, args.streaming)
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
