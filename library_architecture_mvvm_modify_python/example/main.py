import asyncio
import requests
from enum import Enum
from typing import Generic, TypeVar, final
from library_architecture_mvvm_modify_python import debug_print, BaseModel, BaseListModel, NetworkException, Result, LocalException, EnumGuilty, BaseDataForNamed, BaseNamedStreamWState, RWTMode, EnumRWTMode, DefaultStreamWState, NamedCallback,  ExceptionController

class KeysHttpServiceUtility():
    # IPAddress #
    IP_ADDRESS_QQ_IP: str = "ip"

    def __init__(self):
        pass

    def __init__(self):
        pass

class KeysExceptionUtility():
    # UNKNOWN #
    UNKNOWN = "UNKNOWN"

    def __init__(self):
        pass

    def __init__(self):
        pass

class KeysSuccessUtility():
    # SUCCESS #
    SUCCESS = "SUCCESS"

    def __init__(self):
        pass

    def __init__(self):
        pass

class IPAddress(BaseModel):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.IP: str = ip
    
    def get_clone(self) -> 'IPAddress':
        return IPAddress(self.IP)
    
    def to_string(self) -> str:
        return "IPAddress(ip: " + self.IP + ")"

T = TypeVar("T", bound=IPAddress)

class ListIPAddress(Generic[T],BaseListModel[T]):
    def __init__(self, list_model: list[T]) -> None:
        super().__init__(list_model)
    
    def get_clone(self) -> 'ListIPAddress':
        new_list_model = list[T]
        for item_model in self.LIST_MODEL:
            new_list_model.append(item_model.get_clone())
        return ListIPAddress(new_list_model)
    
    def to_string(self) -> str:
        str_list_model = "\n"
        for item_model in self.LIST_MODEL:
            str_list_model += item_model + ",\n"
        return "ListIPAddress(listModel: [" + str_list_model + "])"

### This class needs to be called where there are network requests (in the data source), 
### since without this class the developer will not know in which class the network requests are
@final
class HttpService():
    __instance = None

    def __new__(cls) -> 'HttpService':
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        return cls.__instance

class GetEEIPAddressEEWhereJsonipAPIEEParameterHttpService():
    async def get_ip_address_where_jsonip_api_parameter_http_service() -> Result:
        try:
            response: requests.Response = await requests.request("GET","https://jsonip.com/")
            if response.status_code != 200:
                raise NetworkException.from_key_and_status_code("GetEEIPAddressEEWhereJsonipAPIEEParameterHttpService",str(response.status_code),response.status_code)
            json: dict[str,object] = await response.json()
            ip_address = IPAddress(json.get(KeysHttpServiceUtility.IP_ADDRESS_QQ_IP))
            return Result.success(ip_address)
        except NetworkException as network_exception:
             return Result.exception(network_exception)
        except Exception as exception:
            return Result.exception(LocalException("GetEEIPAddressEEWhereJsonipAPIEEParameterHttpService",EnumGuilty.DEVICE,KeysExceptionUtility.UNKNOWN,str(exception)))
        
@final
class EnumDataForMainVM(Enum):
    IS_LOADING = "isLoading"
    EXCEPTION = "exception"
    SUCCESS = "success"

@final
class DataForMainVM(BaseDataForNamed[EnumDataForMainVM]):
    def __init__(self, is_loading: bool, ip_address: IPAddress) -> None:
        super().__init__(is_loading)
        self.ip_address: IPAddress = ip_address
    
    def get_enum_data_for_named(self) -> EnumDataForMainVM:
        if self.is_loading:
            return EnumDataForMainVM.IS_LOADING
        if self.exception_controller.is_where_not_equals_null_parameter_exception():
            return EnumDataForMainVM.EXCEPTION
        return EnumDataForMainVM.SUCCESS

@final
class MainVM():
    def __init__(self) -> None:
        ## OperationEEModel(EEWhereNamed)[EEFromNamed]EEParameterNamedService
        self.__GET_EE_IP_ADDRESS_EE_WHERE_JSONIP_API_EE_PARAMETER_HTTP_SERVICE = GetEEIPAddressEEWhereJsonipAPIEEParameterHttpService()
        ## NamedUtility
        
        ## Main objects
        self.__NAMED_STREAM_W_STATE: BaseNamedStreamWState[DataForMainVM] = DefaultStreamWState[DataForMainVM](DataForMainVM(True,IPAddress("")))
        self.__RWT_MODE = RWTMode(
            EnumRWTMode.RELEASE,
            [
                NamedCallback("init",self.__init_release_callback)
            ],
            [
                NamedCallback("init",self.__init_test_callback)
            ]
        )
        self.__init_async()
    
    async def __init_async(self) -> None:
        self.__NAMED_STREAM_W_STATE.listen_stream_data_for_named_from_callback(self.__listen_stream_data_w_named_w_callback)
        result = await self.__RWT_MODE.get_named_callback_from_name("init").CALLBACK()
        debug_print("MainVM: " + result)
        self.__NAMED_STREAM_W_STATE.notify_stream_data_for_named()
    
    def __build(self) -> None:
        data_for_named = self.__NAMED_STREAM_W_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForMainVM.IS_LOADING:
                debug_print("Build: IsLoading")
            case EnumDataForMainVM.EXCEPTION:
                debug_print("Build: Exception(" + data_for_named.exception_controller.get_key_parameter_exception() + ")")
            case EnumDataForMainVM.SUCCESS:
                debug_print("Build: Success(" + data_for_named.ip_address + ")")

    def __listen_stream_data_w_named_w_callback(self, _: DataForMainVM) -> None:
        self.__build()
            
    async def __init_release_callback(self) -> str:
        get_ee_ip_address_ee_where_jsonip_api_ee_parameter_http_service = await self.__GET_EE_IP_ADDRESS_EE_WHERE_JSONIP_API_EE_PARAMETER_HTTP_SERVICE.get_ip_address_where_jsonip_api_parameter_http_service()
        if get_ee_ip_address_ee_where_jsonip_api_ee_parameter_http_service.EXCEPTION_CONTROLLER.is_where_not_equals_null_parameter_exception():
            return self.__first_qq_init_release_callback_qq_get_ip_address_where_jsonip_api_parameter_http_service(get_ee_ip_address_ee_where_jsonip_api_ee_parameter_http_service.EXCEPTION_CONTROLLER)
        self.__NAMED_STREAM_W_STATE.get_data_for_named().is_loading = False
        self.__NAMED_STREAM_W_STATE.get_data_for_named().ip_address = get_ee_ip_address_ee_where_jsonip_api_ee_parameter_http_service.PARAMETER.get_clone()
        return KeysSuccessUtility.SUCCESS
         
    async def __init_test_callback(self) -> str:
        ## Simulation get "IPAddress"
        ip_address = IPAddress("121.121.12.12")
        await asyncio.sleep(1)
        self.__NAMED_STREAM_W_STATE.get_data_for_named().is_loading = False
        self.__NAMED_STREAM_W_STATE.get_data_for_named().ip_address = ip_address.get_clone()
        return KeysSuccessUtility.SUCCESS
    
    async def __first_qq_init_release_callback_qq_get_ip_address_where_jsonip_api_parameter_http_service(self,exception_controller: ExceptionController) -> str:
        self.__NAMED_STREAM_W_STATE.get_data_for_named().is_loading = False
        self.__NAMED_STREAM_W_STATE.get_data_for_named().exception_controller = exception_controller
        return exception_controller.get_key_parameter_exception()

def main():
    MainVM()

if __name__ == "__main__":
    main()
## EXPECTED OUTPUT:
##
## MainVM: SUCCESS
## Build: Success(IPAddress(ip: ${your_ip}))

### OR

## EXPECTED OUTPUT:
##
## ===start_to_trace_exception===
##
## WhereHappenedException(Class) --> ${WhereHappenedException(Class)}
## NameException(Class) --> ${NameException(Class)}
## toString() --> ${toString()}
##
## ===end_to_trace_exception===
##
## MainVM: ${getKeyParameterException}
## Build: Exception(${getKeyParameterException})