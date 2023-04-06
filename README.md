# Data Transfer Object (DTO) with interface
### Simple FastAPI project. Use API of site "api.m3o.com".

----

## Table of Contents
* [Installation](#installation)
* [Next Steps](#next-steps)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

----

## 📖 Installation

```
$ git clone https://github.com/lilchiken/dto-with-interface-fastapi.git
$ cd dto-with-interface-fastapi
```

### Pip

```
# Windows
$ python -m venv .venv

# macOS
$ python3 -m venv venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ cd src
(.venv) $ uvicorn main:app
# Load the site at http://127.0.0.1:8000
```

### Docker

```
$ docker pull lilchiken/dto-with-interface
$ docker run -d --name dto-with-interface-container -p 80:80 dto-with-interface
# Load the site at http://localhost:80
```

----

## Next Steps

- Connect another API, try changing the JSON objects for your needs. 
- Add [gunicorn](https://pypi.org/project/gunicorn/) or other web server for improve your skills.
- Configure permissions in API viewset.

----

## 🤝 Contributing

Contributions, issues and feature requests are welcome! ;)

## ⭐️ Support

Give a ⭐️  if this project helped you!

## License

[The MIT License](LICENSE)
