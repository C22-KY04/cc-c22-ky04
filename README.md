## Cloud Architecture Diagram

![](cloud-architecture-diagram.png)

See more [here](https://www.figma.com/file/bXdu32FvMX29idjgUkxKXN/Google-Cloud-Diagram?node-id=0%3A1)

<br><br>

## Optical Character Recognition API

Create REST API using [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/2.1.x/), [Cloud Run](https://cloud.google.com/run), and [Cloud Storage](https://cloud.google.com/storage)

### Base URL

https://ocr-api-5igfi42iaq-et.a.run.app

### Routing

**POST** &nbsp;&nbsp; `/`

This method allows you to classify an image as ID card or not and extract data on ID card.

Request Body &nbsp;&nbsp; `multipart/form-data`

<table>
  <tr>
    <td>file</td>
    <td>File</td>
    <td>png&nbsp;/&nbsp;jpg&nbsp;/&nbsp;jpeg</td>
    <td><b>required</b></td>
  </tr>
</table>

Response &nbsp;&nbsp; `application/json`

HTTP Response Status Codes  &nbsp;&nbsp; **201**

```json
{
    "status": "OK",
    "message": "Successfully extract data with OCR.",
    "data": {
        "province": "DKI JAKARTA",
        "district": "JAKARTA BARAT",
        "id_number": "3173012512720017",
        "name": "ANTONIUS NATANAEL IS",
        "place_date_of_birth": "GISTING 25121972",
        "gender": "LAKILAKI",
        "blood_type": "O",
        "address": "RAWA BUAYA",
        "neighborhood": "008 010",
        "village": "RAWA BUAYA",
        "subdistrict": "CENGKARENG",
        "religion": "KRISTEN",
        "marital_status": "KAWIN",
        "occupation": "KARYAWAN SWASTA",
        "nationality": "WNI",
        "expiry_date": "25122016",
        "attachment": "https://storage.googleapis.com/my-bucket-05062022/07062022-090707.png"
    }
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **400**

```json
{
    "status": "Bad Request",
    "message": "No file part."
}
```

```json
{
    "status": "Bad Request",
    "message": "No selected file."
}
```

HTTP Response Status Codes  &nbsp;&nbsp; **406**

```json
{
    "status": "Not Acceptable",
    "message": "Only files with extension png, jpg, jpeg are allowed."
}
```

```json
{
    "status": "Not Acceptable",
    "message": "That's not an Indonesian ID Card (KTP). Please try again."
}
```

<br><br>

## ID Cards API

Create a REST API using [Node.js](https://nodejs.org/en/), [Express](https://expressjs.com/), [Cloud Run](https://cloud.google.com/run), and [Firestore](https://cloud.google.com/firestore).

### Base URL

https://id-cards-api-yil5spdsaq-et.a.run.app

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
    "attachment": "https://storage.googleapis.com/my-bucket-05062022/04062022-090807.png"
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
            "attachment": "https://storage.googleapis.com/my-bucket-05062022/04062022-090807.png"
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
            "attachment": "https://storage.googleapis.com/my-bucket-05062022/04062022-090807.png"
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
        "attachment": "https://storage.googleapis.com/my-bucket-05062022/04062022-090807.png"
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
    "attachment": "https://storage.googleapis.com/my-bucket-05062022/04062022-090807.png"
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
