# Design of Responsive Website
## AIM:
To design a responsive website with two break points.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>GREAT TECH MATE</title>
</head>

<body>
    <div class="jumbotron jumbotron-fluid" style="background-color: darkslategray;">
        <div class="container text-center"
            style="font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;">
            <h1 class="display-6">GREAT TECH MATE</h1>
            <p class="lead">SMARTER BRINGS US TOGETHER</p>
        </div>
    </div>
    <div class="container  text-center">
        <div class="col-12"><a href='#'>HOME</a>
            <div class="col-12"><a href='#'>DELL LAPTOPS</a>
                <div class="col-12"><a href='#'>HP LAPTOPS</a>
                    <div class="col-12"><a href='#'>ASUS LAPTOPS</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div>
        <div class="row text-center">
            <div class=" col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/d1.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">Dell Vostro 3491 14-inch FHD Laptop</h5>
                    <p class="card-text">RS:43,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/d2.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">Dell G3 3500 Gaming 15.6-inch Laptop</h5>
                    <p class="card-text">RS:77,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/d3.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">Dell Inspiron 3501 15.6-inch FHD Laptop</h5>
                    <p class="card-text">price:RS:59,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/d4.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">Dell Vostro 3405 14 FHD AG Display Laptop </h5>
                    <p class="card-text">RS:52,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/h1.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">HP 15 11th Gen Intel Core i5 15.6-inch FHD Laptop</h5>
                    <p class="card-text">RS:59,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/h2.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">HP 15 Thin & Light 15.6-inch FHD Laptop</h5>
                    <p class="card-text">RS:72,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/h3.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">HP Pavilion x360 Touchscreen 2-in-1 FHD 14-inch Laptop 14-inch Laptop</h5>
                    <p class="card-text">RS:62,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/h4.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">HP Pavilion Gaming 15.6-inch FHD Gaming Laptop</h5>
                    <p class="card-text">RS:77,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/a1.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">ASUS ZenBook Duo UX481FL-BM5811T Intel Core i5 10th Gen 14-inch FHD Thin and
                        Light Laptop </h5>
                    <p class="card-text">RS:87,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/a2.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">ASUS ZenBook 14 (2020) Intel Core i5-1135G7 11th Gen 14-inch FHD Thin and
                        Light Laptop</h5>
                    <p class="card-text">RS:75,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/a3.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">ASUS VivoBook S14 Intel Core i5-1035G1 10th Gen 14-inch FHD Thin and Light
                        Laptop</h5>
                    <p class="card-text">RS:59,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/image/a4.jpg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">ASUS ROG Zephyrus G14, 14" FHD 120Hz, Ryzen 5 4600HS, GeForce GTX 1650Ti 4GB
                        Graphics, Gaming Laptop</h5>
                    <p class="card-text">RS:95,000</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <p>Copyright © 2020 Great Tech Mate, Developed by Khadar basha.</p>
            </div>
        </div>
    </div>




    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>
</html>
```
## OUTPUT:
![output](./static/image/output1.png)
![output](./static/image/output2.jpeg)
![output](./static/image/output3.jpeg)
![output](./static/image/output4.png)
![output](./static/image/output5.png)
![output](./static/image/output6.png)

## CODE VALIDATION REPORT:
![output](./static/image/report1.png)

## RESULT:
Thus a responsive website is designed with two break points and is hosted in the URL http://khadar.student.saveetha.in:8000/. HTML code is validated.