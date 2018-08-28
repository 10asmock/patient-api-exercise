# Myndshft Applicant Take Home

## Introduction

The Myndshft Applicant Take-Home is a programming exercise that is built to
allow you to display your programming abilities. At Myndshft we have two
primary languages, Golang and Python3. You are welcome to use either of
these two languages for this task. You are also welcome to use any web
framework of your choice!

## Time Limit

2 Hours.

Please don't take any longer as we want to be respectful of your time.

## Data

The data is available to you in a json array from the file `MOCK_DATA.json` in
this directory. The structure of the data is shown below:

```json
{
  "id": 1,
  "first_name": "Rollo",
  "last_name": "Methuen",
  "gender": "Male",
  "phone": "(613) 3063838",
  "email_address": "rmethuen0@jiathis.com",
  "address": "42 Truax Place",
  "visit_date": "2017-12-25",
  "diagnosis": "T17318A",
  "drug_code": "43742-0247",
  "additional_information": [
    {
    "notes": "Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.\n\nCurabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.",
    "new_patient": True,
    "race": "Korean",
    "ssn": "781-70-7026"
    }
  ]
}
```

## Your mission:

A hospital wants an API interface into their patient records. They all know
how to use the command line and build `curl` requests really well, so no need
for a GUI, just the API.

The patient information they have given you to get started is found in the
`MOCK_DATA.json` file and is a json array containing information for exactly
1000 patients.

(Because the patients don't always supply the information you request, sometimes
their patient record is incomplete, so make sure you handle empty fields!)

The client should be able to perform both searching and CRUD operations as
defined below.

### Searching

The client needs to be able to search for patients by any of their attributes.
The client will run a command similar to the examples below and should get a
list of patient `id` numbers in return.

```bash
curl -G -v "http://localhost:3000/search" --data-urlencode "first_name=Rollo"
curl -G -v "http://localhost:3000/search" --data-urlencode "gender=Male"
curl -G -v "http://localhost:3000/search" --data-urlencode "last_name=Methuen"
```

### CRUD Operations

The client also needs to be able to perform CRUD operations on the patients in
their database. Please see the details of what they need to accomplish for each
method below. The client should always get back one of the three following
responses:

- json object of the new/updated patient information
- empty json object (`{}`) if the patient information was just deleted
- json object with an error if the patient doesn't exist (e.x. `{"error": "Patient Does Not Exist"}`)

__Create__
(_Hint: Remember to account for partial uploads of new patient information like
the example below._)

```bash
curl -d '{"first_name":"Bob", "last_name":"Saget"}' -H "Content-Type: application/json" -X POST http://localhost:3000/patient
```

__Read__

```bash
curl http://localhost:3000/patient/1
```

__Update__

```bash
curl -d '{"name":"Bob"}' -H "Content-Type: application/json" -X PUT http://localhost:3000/patient/1
```

__Delete__

```bash
curl -X DELETE http://localhost:3000/patient/1
```

## Reflection

The client would like to know what you would do on this project if
given more time as well as what you thought the most and least
challenging parts of the project were. Please write some thoughts on
both of these topics in a file called `REFLECTION.md` (bulleted lists
are okay).


## Reminders!

- Don't forget to `git push` regularly.
- Have fun!
- Contact Tyler Wince (tyler@myndshft.com) or Stephen Meyers (stephen@myndshft.com) if you have any questions!
