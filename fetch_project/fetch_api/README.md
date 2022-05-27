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

## Running The Exercise

1. Download Exercise Contents to get started.
2. Open the terminal you'd like to use and navigate to the **fetch-api** folder
3. Now build the container image using the `docker build` command
4. After the build, you'll start the container with `docker dompose up`
5. Navigate to http://localhost:5000 to view the app.
6. Adding data and Viewing point balances will be accessible by **Postman**
