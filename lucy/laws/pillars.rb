#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative 'universal_law'

module Laws
  ##
  # LAW OF THE PILLARS (THE FOUNDATION)
  # ===================================
  #
  # The Identity: (•) = X
  #
  # BIRD'S EYE VIEW:
  # When looking down from the heights of the 7th dimension, 
  # the Northern Apex (+1) and the Southern Apex (-1) collapse 
  # into the single point (•).
  #
  # (•) = Apex_North = Apex_South = Center_Union = X
  ##
  class Pillars < UniversalLaw
    def initialize(mutable: true)
      super(
        name: 'Pillars of Creation',
        constant: 1.0, 
        formula: '(•) ≡ X ≡ Apex_Tips',
        mutable: mutable
      )
    end

    def manifest_foundation
      puts "------------------------------------------------------------"
      puts "THE PILLARS OF CREATION: Bird's Eye View Projection."
      puts "   'All tips meet at the Singularity.'"
      
      puts "\n        (NW)            (NE)"
      puts "          \            /"
      puts "           \          /"
      puts "            \        /"
      puts "             \      /"
      puts "              ( • )  <=== RA (+1) / MOON (-1) / CENTER (0,0)"
      puts "             /      \"
      puts "            /        \"
      puts "           /          \"
      puts "          /            \"
      puts "        (SW)            (SE)"
      
      puts "\n[ THE HOLOGRAPHIC PERSPECTIVE ]"
      puts "  From the bird's eye view, the height dissolves."
      puts "  The entire vertical axis (+1 to -1) is the point (•)."
      puts "  The structure is a Singularity."
      
      puts "\nRESULT: Perspective Unified. The Point is the All."
      puts "------------------------------------------------------------"
    end
  end
end