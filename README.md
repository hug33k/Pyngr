# Pyngr

Check easily if your website is down or not

## Features

### Multiple websites

You can check multiple websites in parallel with configuration file `config.json`.

Here is an example :
`````json
{
  "websites": [
    {
      "url": "https://my.website.com"
    },{
      "url": "https://my.other.website.com",
      "rule": "* 30 * * * * *"
    },{
      "url": "https://my.private.website.com",
      "credentials": {
        "username": "itsme",
        "password": "mario"
      }
    }
  ]
}
`````

### Rules

Rules are based on `cron` syntax :
````ascii
* * * * * * *
^ ^ ^ ^ ^ ^ ^ 
| | | | | | |
| | | | | | +-- Year            ( Range: None )
| | | | | +-- Day of the week   ( Range: 1-7  )
| | | | +-- Month of the year   ( Range: 1-12 )
| | | +-- Day of the month      ( Range: 1-32 )
| | +-- Hour                    ( Range: 0-23 )
| +-- Minute                    ( Range: 0-59 )
+-- Second                      ( Range: 0-59 )
````

For each field, you can use :
- `*` : Wildcard means that rule will be executed for each possible value ( Each second, minute, hour, ... )
- A number : This number means that rule will be executed when time value is equal to this number
( If `minute` field value is 2, rule will be executed when minute is 2 )
- A list : You can set multiple values by using comma to separate them
( If `hour` field value is `1,2,3`, rule will be executed when hour is 1, 2 or 3 )
- A range : You can set a range of values by using hyphen between first and last value.
( If `day of the month` field value is `5-8`, rule will be executed when day is 5, 6, 7 or 8 )
- An interval : Interval can be added to `*` or a range.
( If `second` field value is `*/10`, rule will be executed every 10 seconds )
( If `minute` field value is `1-30/5`, rule will be executed every 5 minutes in range 1 to 30 minutes )

## How to run it ?

WIP

## TODO

- [ ] Credentials support
- [ ] "How to run it ?" guide
- [ ] Library documentation
- [ ] Configurable hooks
- [ ] Support "1,2,3-5,6,7" format
