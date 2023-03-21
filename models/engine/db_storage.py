class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(hbnb_dev, hbnb_dev_pwd, hbnb_dev_db),
                           pool_pre_ping=True)
    def all(self, cls=None):
        pass
    def new(self, obj):
        self.__session = session.add(obj)

    def save(self):
        self.__session = session.commit()

    def delete(self, obj=None):
        if not None:
            session.delete(obj)
    def reload(self):
        pass
    

