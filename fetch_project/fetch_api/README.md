# Fetch Rewards Coding Exercise

## Usage
 
 All Responses will have the form

 ```json
 {
     "data":"Mixed type holding the content of the response",
     "message": "Description of what happened"
 }
```
 
 Subsequent resposne definitions will only detail the expected value of the 'data field'

 ### List of Payers and Point Balances

 **Definition**

 `GET /payers`

 **Response**

 -`200 OK` on success

 ```json
 [
     {
         "payer": "Dannon",
         "points": 1000,
         "timestamp": "2020-11-02T14:00:00Z"
     },
     {
         "payer": "Unilever",
         "points": 200,
         "timestamp": "2020-11-02T14:00:00Z"
     },
     {
         "payer": "Dannon",
         "points": -200,
         "timestamp": "2020-11-02T14:00:00Z"
     }
 ]
 ```

 
### Adding a transaction for a specific payer and date

**Definition**

`POST /payers`

**Arguments**
- `"payer": string` company name 
- `"points": integer` points earned from transaction
- `"timestamp": date` date that the transaction occured

**Response**

 -`201 Created` on success

```json
{
    "payer": "Dannon",
    "points": 1000,
    "timestamp": "2020-11-02T14:00:00Z"
}
```

### Spend Points 

**Definition**

`POST /payers`

**Arguments**
- `"points": integer` points to spend for rewards

**Response**

 -`200 OK` on success

```json
[
    { "payer": "DANNON", "points": -100 },
    { "payer": "UNILEVER", "points": -200 },
    { "payer": "MILLER COORS", "points": -4700 }
]
```