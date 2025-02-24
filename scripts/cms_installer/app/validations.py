from pydantic import BaseModel, FilePath, ValidationError, IPvAnyAddress

from app.models import UnixName, EmailString, DomainName, NodePath


class FilePathField(BaseModel):
    filepath: FilePath

    @staticmethod
    def from_input(value: str) -> bool:
        try:
            FilePathField(filepath=value)
            return True
        except ValidationError:
            return False


class UnixNameField(BaseModel):
    username: UnixName

    @staticmethod
    def from_input(value: str) -> bool:
        try:
            UnixNameField(username=value)
            return True
        except ValidationError:
            return False


class EmailStringField(BaseModel):
    email: EmailString

    @staticmethod
    def from_input(value: str) -> bool:
        try:
            EmailStringField(email=value)
            return True
        except ValidationError:
            return False


class IPAddressesField(BaseModel):
    ip1: IPvAnyAddress

    @staticmethod
    def from_input(value: str) -> bool:
        try:
            IPAddressesField(ip1=value)
        except ValidationError:
            return False
        return True


class DomainNameField(BaseModel):
    domain: DomainName

    @staticmethod
    def from_input(value: str) -> bool:
        try:
            DomainNameField(domain=value)
            return True
        except ValidationError:
            return False


class NodePathField(BaseModel):
    path: NodePath

    @staticmethod
    def from_input(value: str) -> bool:
        try:
            NodePathField(path=value)
            return True
        except ValidationError:
            return False


def check_file_name(path: str, expected_file_name: str) -> bool:
    return path.endswith(expected_file_name) and FilePathField.from_input(path)


def check_sdc_key_path(value: str) -> bool:
    return check_file_name(value, "consumerLeaf1.key")


def check_sdc_certificate_path(value: str) -> bool:
    return check_file_name(value, "consumerLeaf1.crt")


def check_sdc_intermediate_certificate_path(value: str) -> bool:
    return check_file_name(value, "intermediateCA.crt")
