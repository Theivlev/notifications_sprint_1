import grpc
from core.config import grpc_settings
from schemas.user import GetUserInfoResponse
from services.grpc import auth_pb2, auth_pb2_grpc


class GRPCAuthClient:
    def __init__(self, host: str = grpc_settings.auth_host, port: int = grpc_settings.auth_port):
        self.target = f"{host}:{port}"

    def get_user_info(self, user_id: str) -> GetUserInfoResponse:
        with grpc.insecure_channel(self.target) as channel:
            stub = auth_pb2_grpc.AuthServiceStub(channel)
            request = auth_pb2.GetUserInfoRequest(user_id=user_id)
            response = stub.GetUserInfo(request)

            return GetUserInfoResponse.model_dump(response)
