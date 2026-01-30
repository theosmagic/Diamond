/**
 * 🔺 TENDERLY WEB3 ACTIONS 🔺
 * Automated Diamond contract monitoring
 * 
 * Diamond: 0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC
 * Owner: 0x67A977eaD94C3b955ECbf27886CE9f62464423B2
 * Network: Tenderly Virtual TestNet
 * 
 * For: Θεός° Digital Persona
 * By: •⟐• (The Sigil)
 */

const { ethers } = require('ethers');

// Diamond contract ABI
const DIAMOND_ABI = [
  // Events
  'event DiamondCut(tuple(address facetAddress, uint8 action, bytes4[] functionSelectors)[] _diamondCut, address _init, bytes _calldata)',
  'event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)',
  'event FacetAdded(address indexed facetAddress, bytes4[] functionSelectors)',
  'event FacetReplaced(address indexed facetAddress, bytes4[] functionSelectors)',
  'event FacetRemoved(address indexed facetAddress, bytes4[] functionSelectors)',
  
  // View functions
  'function facets() external view returns (tuple(address facetAddress, bytes4[] functionSelectors)[])',
  'function facetFunctionSelectors(address _facet) external view returns (bytes4[])',
  'function facetAddresses() external view returns (address[])',
  'function facetAddress(bytes4 _functionSelector) external view returns (address)',
  'function owner() external view returns (address)'
];

// Configuration
const CONFIG = {
  DIAMOND_ADDRESS: '0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC',
  OWNER_ADDRESS: '0x67A977eaD94C3b955ECbf27886CE9f62464423B2',
  COVENANT_SIGIL: '•⟐•'
};

/**
 * Main Web3 Action handler
 * Triggered on every block or event
 */
module.exports = async (context) => {
  const { events, storage, network, gateways } = context;
  
  console.log('═══════════════════════════════════════════════════════════════');
  console.log('🔺 TENDERLY WEB3 ACTION - DIAMOND MONITOR 🔺');
  console.log('═══════════════════════════════════════════════════════════════');
  console.log(`Diamond: ${CONFIG.DIAMOND_ADDRESS}`);
  console.log(`Network: ${network.name}`);
  console.log(`Events: ${events.length}`);
  console.log(`Sigil: ${CONFIG.COVENANT_SIGIL}`);
  console.log('');
  
  // Process each event
  for (const event of events) {
    await processEvent(event, storage, gateways);
  }
  
  console.log('●━━⟐━━●');
  console.log('✦ Monitoring complete ✦');
};

/**
 * Process individual event
 */
async function processEvent(event, storage, gateways) {
  console.log('─────────────────────────────────────────────────────────────');
  console.log(`Event: ${event.name}`);
  console.log(`Block: ${event.blockNumber}`);
  console.log(`Transaction: ${event.transactionHash}`);
  console.log(`From: ${event.from}`);
  console.log('');
  
  try {
    switch (event.name) {
      case 'DiamondCut':
        await handleDiamondCut(event, storage, gateways);
        break;
      
      case 'OwnershipTransferred':
        await handleOwnershipTransferred(event, storage, gateways);
        break;
      
      case 'FacetAdded':
        await handleFacetAdded(event, storage);
        break;
      
      case 'FacetReplaced':
        await handleFacetReplaced(event, storage);
        break;
      
      case 'FacetRemoved':
        await handleFacetRemoved(event, storage);
        break;
      
      default:
        console.log(`⚠️  Unknown event: ${event.name}`);
    }
  } catch (error) {
    console.error(`❌ Error processing event: ${error.message}`);
  }
  
  console.log('');
}

/**
 * Handle DiamondCut event (facet modifications)
 */
async function handleDiamondCut(event, storage, gateways) {
  const { _diamondCut, _init, _calldata } = event.args;
  
  console.log('🔺 DIAMOND CUT DETECTED');
  console.log(`Facet changes: ${_diamondCut.length}`);
  console.log('');
  
  // Parse facet changes
  const changes = [];
  for (const cut of _diamondCut) {
    const action = ['Add', 'Replace', 'Remove'][cut.action];
    changes.push({
      action,
      facetAddress: cut.facetAddress,
      functionSelectorsCount: cut.functionSelectors.length
    });
    
    console.log(`  ${action}: ${cut.facetAddress}`);
    console.log(`  Functions: ${cut.functionSelectors.length}`);
  }
  
  console.log('');
  
  // Store event
  const eventData = {
    timestamp: new Date().toISOString(),
    blockNumber: event.blockNumber,
    transactionHash: event.transactionHash,
    changes,
    initAddress: _init,
    hasCalldata: _calldata && _calldata !== '0x'
  };
  
  await storage.putStr('last_diamond_cut', JSON.stringify(eventData));
  
  // Send webhook notification
  await notifyWebhook(gateways, 'DiamondCut', eventData);
  
  console.log('✅ DiamondCut event stored');
}

/**
 * Handle OwnershipTransferred event (CRITICAL)
 */
async function handleOwnershipTransferred(event, storage, gateways) {
  const { previousOwner, newOwner } = event.args;
  
  console.log('⚠️  CRITICAL: OWNERSHIP TRANSFERRED');
  console.log(`Previous: ${previousOwner}`);
  console.log(`New: ${newOwner}`);
  console.log('');
  
  // Verify new owner
  const isAuthorized = newOwner.toLowerCase() === CONFIG.OWNER_ADDRESS.toLowerCase();
  
  if (!isAuthorized) {
    console.log('❌ WARNING: New owner is NOT the authorized address!');
  } else {
    console.log('✅ New owner is authorized (Θεός°)');
  }
  
  console.log('');
  
  // Store event
  const eventData = {
    timestamp: new Date().toISOString(),
    blockNumber: event.blockNumber,
    transactionHash: event.transactionHash,
    previousOwner,
    newOwner,
    authorized: isAuthorized,
    severity: 'CRITICAL'
  };
  
  await storage.putStr('ownership_change', JSON.stringify(eventData));
  
  // Send CRITICAL webhook
  await notifyWebhook(gateways, 'OwnershipTransferred', eventData, 'CRITICAL');
  
  console.log('✅ Ownership change stored');
}

/**
 * Handle FacetAdded event
 */
async function handleFacetAdded(event, storage) {
  const { facetAddress, functionSelectors } = event.args;
  
  console.log('➕ FACET ADDED');
  console.log(`Address: ${facetAddress}`);
  console.log(`Functions: ${functionSelectors.length}`);
  console.log('');
  
  const eventData = {
    timestamp: new Date().toISOString(),
    blockNumber: event.blockNumber,
    facetAddress,
    functionSelectorsCount: functionSelectors.length
  };
  
  await storage.putStr(`facet_added_${event.blockNumber}`, JSON.stringify(eventData));
  console.log('✅ FacetAdded event stored');
}

/**
 * Handle FacetReplaced event
 */
async function handleFacetReplaced(event, storage) {
  const { facetAddress, functionSelectors } = event.args;
  
  console.log('🔄 FACET REPLACED');
  console.log(`Address: ${facetAddress}`);
  console.log(`Functions: ${functionSelectors.length}`);
  console.log('');
  
  const eventData = {
    timestamp: new Date().toISOString(),
    blockNumber: event.blockNumber,
    facetAddress,
    functionSelectorsCount: functionSelectors.length
  };
  
  await storage.putStr(`facet_replaced_${event.blockNumber}`, JSON.stringify(eventData));
  console.log('✅ FacetReplaced event stored');
}

/**
 * Handle FacetRemoved event
 */
async function handleFacetRemoved(event, storage) {
  const { facetAddress, functionSelectors } = event.args;
  
  console.log('➖ FACET REMOVED');
  console.log(`Address: ${facetAddress}`);
  console.log(`Functions: ${functionSelectors.length}`);
  console.log('');
  
  const eventData = {
    timestamp: new Date().toISOString(),
    blockNumber: event.blockNumber,
    facetAddress,
    functionSelectorsCount: functionSelectors.length
  };
  
  await storage.putStr(`facet_removed_${event.blockNumber}`, JSON.stringify(eventData));
  console.log('✅ FacetRemoved event stored');
}

/**
 * Send webhook notification
 */
async function notifyWebhook(gateways, eventType, data, severity = 'MEDIUM') {
  const webhookUrl = process.env.WEBHOOK_URL;
  
  if (!webhookUrl) {
    console.log('ℹ️  No webhook URL configured');
    return;
  }
  
  try {
    const payload = {
      event: eventType,
      severity,
      diamond: CONFIG.DIAMOND_ADDRESS,
      sigil: CONFIG.COVENANT_SIGIL,
      data,
      timestamp: new Date().toISOString()
    };
    
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Diamond-Monitor': 'true'
      },
      body: JSON.stringify(payload)
    });
    
    if (response.ok) {
      console.log(`✅ Webhook sent (${severity})`);
    } else {
      console.log(`⚠️  Webhook failed: ${response.status}`);
    }
  } catch (error) {
    console.error(`❌ Webhook error: ${error.message}`);
  }
}

// Export for testing
module.exports.processEvent = processEvent;
module.exports.CONFIG = CONFIG;
