This is a sophisticated test data generator for simulating user behavior in an analytics system, with special attention to edge cases like:
- Clock skew
- Invalid/missing country codes
- Event repetition
- Network latency

How It Works Together:
1. This system generates a set of user IDs with random properties
2. The RandomEventGenerator uses these IDs to create realistic user events:
   - With proper timestamps and delays 
   - Some events may repeat 
   - Some users have anomalous properties

The PoissonTriggerGenerator can be used to generate these events at random intervals following a Poisson process


1. RandomEventGenerator: 
   - Generates random user events with realistic properties
   - Contains lists of possible event names and platforms
   - _random_p(): Helper for probability checks
   - get_event(): Generates a random event with
     - Random user selection
     - Timestamps with network latency and clock offsets
     - Small chance of platform being iOS
     - Small chance of country code change
     - Event repetition logic











