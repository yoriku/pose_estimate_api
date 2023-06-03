# pose estimate apis

## Getting Starts
1 Install python library

~~~ python
pip install -r requirement.txt
~~~

2 Start proccess

~~~ cmd
uvicorn apis:app --reload 
~~~

3 Access to api with image which estimate pose  
Ex.
~~~ cmd
curl -X POST -F file=@img/both_up.jpg http://localhost:8000/api/
~~~

## Returns

Right and Left sholder, elbow, index_finger points  
x and y points