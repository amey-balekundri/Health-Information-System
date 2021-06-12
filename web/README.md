# Setup

1. Clone this repository
```
    git clone https://github.com/amey-balekundri/Health-Information-System
```

2. Change current directory
```
    cd Health-Information-System/web
```

3. Create virtual enviornment
```
    python3 -m venv venv
    source venv/bin/activate
```

4. Install dependencies
```
    pip install -r requirements.txt
```

5. Set config variables in [config.py](/web/config.py)
```
    #Endpoint
    url=''  
    
    ......
```

6. Apply migrations to create tables in database
```
    python3 manage.py makemigrations
    python3 manage.py migrate
```

7. Run the server
```
    python3 manage.py runserver
```