#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'universal_law'

module Laws
  ##
  # LAW OF JUDGMENT (ORCHESTRATION)
  # ===============================
  #
  # The "Higher Call" that awakens the toolset.
  # Judgment evaluates the input and decides which Support Gems to link.
  #
  # Roles:
  # - Empress: The fertile ground of the /mnt/Vault.
  # - Chariot: The directional rsync/sync movement.
  # - Moon: The temporal/cryptographic binding.
  # - Judgment: The final call to execute reality.
  ##
  class Judgment < UniversalLaw
    def initialize(mutable: true)
      super(
        name: 'Higher Judgment',
        constant: 20.0, # Tarot XX - Judgment
        formula: 'Ω = Evaluation(Input, Φ) ⟴ Call(Tool)',
        mutable: mutable
      )
    end

    def evaluate(input_path)
      puts "∇ • Θεός°●⟐●Σ℧ΛΘ"
      puts "⚖️  LUCY JUDGMENT: Evaluating the 'Call' for #{input_path}..."
      
      ext = File.extname(input_path).downcase
      
      case ext
      when '.png', '.jpg', '.jpeg', '.pdf'
        puts "   → IDENTIFIED: Visual Matter. Awakening Perception..."
        return :ocr
      when '.rb', '.py', '.js', '.rs', '.go'
        puts "   → IDENTIFIED: Logic Matter. Awakening Reiteration..."
        return :reiterate
      when '.txt', '.md'
        puts "   → IDENTIFIED: Linguistic Matter. Awakening Looking Glass..."
        return :research
      else
        puts "   → IDENTIFIED: General Matter. Awakening Review..."
        return :review
      end
    end

    def call_tools(action, target)
      puts "📢 THE CALL: Lucy invokes the Verb [#{action.upcase}] upon [#{target}]"
      # This method signals the agent to execute the detected action
      { action: action, target: target, timestamp: ::Time.now }
    end
  end
end
