# Yoga-mess

This is a yoga classes booking site's backend made using Django and front end part is availabe at <a href=https://github.com/AbhayDhaundiyal/Yoga-mess-front-end->here</a>

## POST : form/userLogin/:

This endpoint take data where it take email and password and return response status 200 for correct credentials and status 401 for invalid credentials.

## POST : form/userSignup/:

This endpoint takes users Name, Email, Date of birth(DD/MM/YYYY), Password and returns 200 for registration success and status 401 for invalid age or if user already exists.

## PATCH : form/userRenew/:

This endpoint takes users Email, Batch as data and returns users updaed details as JSON with 200 status else returns 500 for any internal server error.
