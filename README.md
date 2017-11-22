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
* * * * *
^ ^ ^ ^ ^ 
| | | | |
| | | | +-- Day of the month    ( Range: 1-31 )
| | | +---- Day of the week     ( Range: 1-7  )
| | +------ Hour                ( Range: 0-23 )
| +-------- Minute              ( Range: 0-59 )
+---------- Second              ( Range: 0-59 )
````

For each field, you can use :
- `*` : Wildcard means that rule will be executed for each possible value ( Each second, minute, hour, ... )
- A number : This number means that rule will be executed when time value is equal to this number
( If `minute` field value is 2, rule will be executed when minute is 2 )
- A list : You can set multiple values by using comma to separate them
( If `hour` field value is `1,2,3`, rule will be executed when hour is 1, 2 or 3 )
- A range : You can set a range of values by using hyphen between first and last value.
( If `day of the month` field value is `5-8`, rule will be executed when day is 5, 6, 7 or 8 )
- An interval : Interval can be added to anything ( Except wildcard ) and its value is any number in available range
( If `second` field value is `*/10`, rule will be executed every 10 seconds )
( If `minute` field value is `1-30/5`, rule will be executed every 5 minutes in range 1 to 30 minutes )

Example of rules :
````ascii
* * * * *
=> Each second
    of each minute
    of each hour
    of each day
    of week/month

0 0 0 1 *
=> At 0:00:00
    each Monday
    of each month

*/30 * * 1-5 1-7
=> Every 30 seconds
    of each minute
    of each hour
    from Monday to Friday
    in first (complete or partial) week
    of each month
    ( If month start a Wednesday, if will be executed from Wednesday to Friday )

0 */15 0-6/2,6-18,18-23/2 1-5 *
=> First second
    of each quarter
    of every two hours between 0 and 6 or each hour between 6 and 18 or every two hours between 18 and 23
    from Monday to Friday
    of each month
````

## How to run it ?

WIP

## TODO

- [ ] Credentials support
- [ ] "How to run it ?" guide
- [ ] Library documentation
- [ ] Configurable hooks
- [ ] Support valid formats
    - [ ] Lists with nested range
    - [ ] Range with intervals
- [ ] Support invalid formats
    - [ ] "*/0"
    - [ ] "{number}/{number}"
    - [ ] "{number}/*"
