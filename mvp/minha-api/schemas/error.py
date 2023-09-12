from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ mensagem de erro
    """
    mesage: str
