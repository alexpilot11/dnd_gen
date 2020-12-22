# dnd_gen

A library to generate planets for a space-based TTRPG hex-crawl campaign

## Setup
1. install virtualenvwrapper
2. `mkvirtualenv planet -r requirements.txt`
3. `workon planet`
4. `setprojectdir .`
5. `pip install -e .`


## Usage
`python gen_planet`
- defaults to 5 generated planets

`python gen_planet <num_planets:int>`
- generates the number of planets specified
