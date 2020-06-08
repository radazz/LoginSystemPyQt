# PyQt5 + mysql database connection

easy implementation of mysql database to python
```
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'users'
        }

        self.getattributes = (
            "SELECT `username`, `password`, `HWID` FROM `users`"
        )

        self.database_info = mysql.connector.connect(**self.config)

        self.db = self.database_info.cursor()
        self.db.execute(self.getattributes)
```
