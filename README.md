## Optical Character Recognition API

Create REST API using [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/2.1.x/), and [Cloud Storage](https://cloud.google.com/storage)

## ID Card API

Create a REST API using [Node.js](https://nodejs.org/en/), [Express](https://expressjs.com/), and [Firestore](https://cloud.google.com/firestore).

### Routing

**POST** &nbsp;&nbsp; `/id_cards`

This method allows you to create ID Card.

Authentication

- [x] ID Tokens

Headers

<table>
  <tr>
    <td>Authorization</td>
    <td>string</td>
    <td>Bearer &lt;ID Tokens&gt;</td>
    <td><b>required</b></td>
  </tr>
</table>

Request Body &nbsp;&nbsp; `application/json`

```json
{
    "uid": "q6fvJpSVtIhS2XGqqH8L",
    "province": "JAWA TIMUR",
    "district": "KABUPATEN SIDOARJO",
    "id_number": "351XXXXXXXXXXXXX",
    "name": "MOCHAMMAD ARYA SALSABILA",
    "place_date_of_birth": "SIDOARJO, 24-06-2001",
    "gender": "LAKI-LAKI",
    "blood_type": "-",
    "address": "NGABAN",
    "neighborhood": "005/002",
    "village": "NGABAN",
    "subdistrict": "TANGGULANGIN",
    "religion": "ISLAM",
    "marital_status": "BELUM KAWIN",
    "occupation": "PELAJAR/MAHASISWA",
    "nationality": "WNI",
    "expiry_date": "SEUMUR HIDUP",
    "attachment": "https://www.example.com/"
}
```

Response &nbsp;&nbsp; `application/json`

HTTP Response Status Codes  &nbsp;&nbsp; **201**

```json
{
    "status": "Created",
    "message": "The item/record was created successfully."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **400**

```json
{
    "status": "Bad Request",
    "message": "Error message..."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **401**

```json
{
    "status": "Unauthorized",
    "message": "You do not have permissions to access the service."
}
```

<br><br>

**GET** &nbsp;&nbsp; `/id_cards`

This method allows you to retrieve the entire ID Cards / retrieve some ID Cards by name.

Authentication

- [x] ID Tokens

Headers

<table>
  <tr>
    <td>Authorization</td>
    <td>string</td>
    <td>Bearer &lt;ID Tokens&gt;</td>
    <td><b>required</b></td>
  </tr>
</table>

Query String

<table>
  <tr>
    <td>name</td>
    <td>string</td>
    <td>Pass a text query to search</td>
    <td>optional</td>
  </tr>
</table>

Response &nbsp;&nbsp; `application/json`

HTTP Response Status Codes  &nbsp;&nbsp; **200**

```json
{
    "status": "OK",
    "message": "The items/records was retrieved successfully.",
    "data": [
        {
            "uid": "q6fvJpSVtIhS2XGqqH8L",
            "province": "JAWA TIMUR",
            "district": "KABUPATEN SIDOARJO",
            "id_number": "351XXXXXXXXXXXXX",
            "name": "MOCHAMMAD ARYA SALSABILA",
            "place_date_of_birth": "SIDOARJO, 24-06-2001",
            "gender": "LAKI-LAKI",
            "blood_type": "-",
            "address": "NGABAN",
            "neighborhood": "005/002",
            "village": "NGABAN",
            "subdistrict": "TANGGULANGIN",
            "religion": "ISLAM",
            "marital_status": "BELUM KAWIN",
            "occupation": "PELAJAR/MAHASISWA",
            "nationality": "WNI",
            "expiry_date": "SEUMUR HIDUP",
            "attachment": "https://www.example.com/"
        },
        {
            "uid": "q6fvJpSVtIhS2XGqqH8L",
            "province": "JAWA TIMUR",
            "district": "KABUPATEN SIDOARJO",
            "id_number": "351XXXXXXXXXXXXX",
            "name": "MOCHAMMAD ARYA SALSABILA",
            "place_date_of_birth": "SIDOARJO, 24-06-2001",
            "gender": "LAKI-LAKI",
            "blood_type": "-",
            "address": "NGABAN",
            "neighborhood": "005/002",
            "village": "NGABAN",
            "subdistrict": "TANGGULANGIN",
            "religion": "ISLAM",
            "marital_status": "BELUM KAWIN",
            "occupation": "PELAJAR/MAHASISWA",
            "nationality": "WNI",
            "expiry_date": "SEUMUR HIDUP",
            "attachment": "https://www.example.com/"
        }
    ]
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **400**

```json
{
    "status": "Bad Request",
    "message": "Error message..."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **401**

```json
{
    "status": "Unauthorized",
    "message": "You do not have permissions to access the service."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **404**

```json
{
    "status": "Not Found",
    "message": "The item/record not found."
}
```

<br><br>

**GET** &nbsp;&nbsp; `/id_cards/:uid`

This method allows you to retrieve ID Card details.

Authentication

- [x] ID Tokens

Path Parameters

<table>
  <tr>
    <td>uid</td>
    <td>string</td>
    <td>A unique user ID</td>
    <td><b>required</b></td>
  </tr>
</table>

Headers

<table>
  <tr>
    <td>Authorization</td>
    <td>string</td>
    <td>Bearer &lt;ID Tokens&gt;</td>
    <td><b>required</b></td>
  </tr>
</table>

Response &nbsp;&nbsp; `application/json`

HTTP Response Status Codes  &nbsp;&nbsp; **200**

```json
{
    "status": "OK",
    "message": "The item/record was retrieved successfully.",
    "data": {
        "uid": "q6fvJpSVtIhS2XGqqH8L",
        "province": "JAWA TIMUR",
        "district": "KABUPATEN SIDOARJO",
        "id_number": "351XXXXXXXXXXXXX",
        "name": "MOCHAMMAD ARYA SALSABILA",
        "place_date_of_birth": "SIDOARJO, 24-06-2001",
        "gender": "LAKI-LAKI",
        "blood_type": "-",
        "address": "NGABAN",
        "neighborhood": "005/002",
        "village": "NGABAN",
        "subdistrict": "TANGGULANGIN",
        "religion": "ISLAM",
        "marital_status": "BELUM KAWIN",
        "occupation": "PELAJAR/MAHASISWA",
        "nationality": "WNI",
        "expiry_date": "SEUMUR HIDUP",
        "attachment": "https://www.example.com/"
    }
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **400**

```json
{
    "status": "Bad Request",
    "message": "Error message..."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **401**

```json
{
    "status": "Unauthorized",
    "message": "You do not have permissions to access the service."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **404**

```json
{
    "status": "Not Found",
    "message": "The item/record not found."
}
```

<br><br>

**PUT** &nbsp;&nbsp; `/id_cards/:uid`

This method allows you to update ID Card.

Authentication

- [x] ID Tokens

Path Parameters

<table>
  <tr>
    <td>uid</td>
    <td>string</td>
    <td>A unique user ID</td>
    <td><b>required</b></td>
  </tr>
</table>

Headers

<table>
  <tr>
    <td>Authorization</td>
    <td>string</td>
    <td>Bearer &lt;ID Tokens&gt;</td>
    <td><b>required</b></td>
  </tr>
</table>

Request Body &nbsp;&nbsp; `application/json`

```json
{
    "uid": "q6fvJpSVtIhS2XGqqH8L",
    "province": "JAWA TIMUR",
    "district": "KABUPATEN SIDOARJO",
    "id_number": "351XXXXXXXXXXXXX",
    "name": "MOCHAMMAD ARYA SALSABILA",
    "place_date_of_birth": "SIDOARJO, 24-06-2001",
    "gender": "LAKI-LAKI",
    "blood_type": "-",
    "address": "NGABAN",
    "neighborhood": "005/002",
    "village": "NGABAN",
    "subdistrict": "TANGGULANGIN",
    "religion": "ISLAM",
    "marital_status": "BELUM KAWIN",
    "occupation": "PELAJAR/MAHASISWA",
    "nationality": "WNI",
    "expiry_date": "SEUMUR HIDUP",
    "attachment": "https://www.example.com/"
}
```

Response &nbsp;&nbsp; `application/json`

HTTP Response Status Codes  &nbsp;&nbsp; **200**

```json
{
    "status": "OK",
    "message": "The item/record was updated successfully."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **400**

```json
{
    "status": "Bad Request",
    "message": "Error message..."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **401**

```json
{
    "status": "Unauthorized",
    "message": "You do not have permissions to access the service."
}
```

<br><br>

**DELETE** &nbsp;&nbsp; `/id_cards/:uid`

This method allows you to delete ID Card.

Authentication

- [x] ID Tokens

Path Parameters

<table>
  <tr>
    <td>uid</td>
    <td>string</td>
    <td>A unique user ID</td>
    <td><b>required</b></td>
  </tr>
</table>

Headers

<table>
  <tr>
    <td>Authorization</td>
    <td>string</td>
    <td>Bearer &lt;ID Tokens&gt;</td>
    <td><b>required</b></td>
  </tr>
</table>

Response &nbsp;&nbsp; `application/json`

HTTP Response Status Codes  &nbsp;&nbsp; **200**

```json
{
    "status": "OK",
    "message": "The item/record was deleted successfully."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **400**

```json
{
    "status": "Bad Request",
    "message": "Error message..."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **401**

```json
{
    "status": "Unauthorized",
    "message": "You do not have permissions to access the service."
}
```
