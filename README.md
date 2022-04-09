# AstroPlanner

Viewing conditions and visible objects forecast API

The aim is to have a single service that provides information regarding good astronomy targets on a given night, based on target position and weather conditions in the area.

The first goal is to create a functional API, which will later be supplemented with a simple React frontend and daily email notification service.

Behind the scenes, the purpose is to practice TDD and general project management skills within a React/Django/Python stack.

## RoadMap

### Phase 1

-   Project Set Up - infrastructure, dev environment set up, etc.

-   Connect to OpenWeather API

-   Connect to Astronomy API

### Phase 2

-   Digest OpenWeather API

-   Determine viewing conditions based on weather conditions at coordinates

-   Collect viewing conditions result and relevant OpenWeather data points

### Phase 3

-   Digest Astronomy API

-   Get positions of objects and process relevant information into JSON

-   Calculate actualVisibility
