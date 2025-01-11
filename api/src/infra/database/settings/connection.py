from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHanlder:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        if self.__engine is None:
            self.__engine = create_engine(self.__connection_string)
            print("Engine criado:", self.__engine)

    def get_engine(self):
        self.connect_to_db()  # Certifique-se de que o engine foi inicializado
        return self.__engine

    def __enter__(self):
        self.connect_to_db()
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()


db_connection_handler = DBConnectionHanlder()
