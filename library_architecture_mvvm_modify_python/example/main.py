import asyncio
import requests
from enum import Enum
from typing import Generic, TypeVar, final
from library_architecture_mvvm_modify_python import *

@final
class ReadyDataUtility():
    UNKNOWN: str = "UNKNOWN"
    SUCCESS: str = "SUCCESS"
    IP_API: str = "https://jsonip.com/"

    def __init__(self):
        pass

    def __init__(self):
        pass

@final
class KeysHttpServiceUtility():
    # IPAddress #
    IP_ADDRESS_QQ_IP: str = "ip"

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
        new_list_model: list[T] = []
        for item_model in self.LIST_MODEL:
            new_list_model.append(item_model.get_clone())
        return ListIPAddress(new_list_model)
    
    def to_string(self) -> str:
        str_list_model = "\n"
        for item_model in self.LIST_MODEL:
            str_list_model += item_model.to_string() + ",\n"
        return "ListIPAddress(listModel: [" + str_list_model + "])"
    
Y = TypeVar("Y", bound=ListIPAddress)    

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

class IPAddressRepository(Generic[T,Y], BaseModelRepository[T,Y]):
    def __init__(self, enum_rwt_mode: EnumRWTMode) -> None:
        super().__init__(enum_rwt_mode)
        self._http_service: HttpService = HttpService()
    
    def _get_base_model_from_map_and_list_keys(self, map: dict[str, object], list_keys: list[str]) -> T:
        if len(list_keys) <= 0:
            return IPAddress("")
        if(map.get(list_keys[0]) is None):
            return IPAddress("")
        return IPAddress(map.get(list_keys[0]))
    
    def _get_base_list_model_from_list_model(self, list_model: list[T]) -> Y:
        return ListIPAddress(list_model)
    
    async def get_ip_address_parameter_http_service(self) -> Result:
        return await self._get_mode_callback_from_release_callback_and_test_callback_parameter_enum_rwt_mode(
            self.__get_ip_address_parameter_http_service_w_release_callback,
            self.__get_ip_address_parameter_http_service_w_test_callback)()
    
    async def __get_ip_address_parameter_http_service_w_release_callback(self) -> Result:
        try:
            response: requests.Response = requests.request("GET",ReadyDataUtility.IP_API)
            if response.status_code != 200:
                raise NetworkException.from_key_and_status_code("IPAddressRepository",str(response.status_code),response.status_code)
            json: dict[str,object] = response.json()
            return Result.success(self._get_base_model_from_map_and_list_keys(
                json,[KeysHttpServiceUtility.IP_ADDRESS_QQ_IP]))
        except NetworkException as network_exception:
             return Result.exception(network_exception)
        except Exception as exception:
            return Result.exception(LocalException("IPAddressRepository",EnumGuilty.DEVICE,ReadyDataUtility.UNKNOWN,str(exception)))
    
    async def __get_ip_address_parameter_http_service_w_test_callback(self) -> Result:
        await asyncio.sleep(1)
        return Result.success(self._get_base_model_from_map_and_list_keys(
            {KeysHttpServiceUtility.IP_ADDRESS_QQ_IP : "121.121.12.12"},
            [KeysHttpServiceUtility.IP_ADDRESS_QQ_IP]))
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
    
    def to_string(self) -> str:
        return "DataForMainVM(is_loading: " + str(self.is_loading) + ", " + "exception_controller: " + self.exception_controller.to_string() + ", " + "ip_address: " + self.ip_address.to_string() + ")"

@final
class MainVM():
    def __init__(self) -> None:
        ## ModelRepository
        self.__IP_ADDRESS_REPOSITORY: IPAddressRepository = IPAddressRepository(EnumRWTMode.RELEASE)
        
        ## NamedUtility
        
        ## NamedStreamWState 
        self.__NAMED_STREAM_W_STATE: BaseNamedStreamWState[DataForMainVM] = DefaultStreamWState[DataForMainVM](DataForMainVM(True,IPAddress("")))
    
    async def init(self) -> None:
        self.__NAMED_STREAM_W_STATE.listen_stream_data_for_named_from_callback(self.__listen_stream_data_w_named_w_callback)
        first_request = await self.__first_request()
        debug_print("MainVM: " + first_request)
        self.__NAMED_STREAM_W_STATE.notify_stream_data_for_named()

    def dispose(self) -> None:
        self.__NAMED_STREAM_W_STATE.dispose()
    
    def __build(self) -> None:
        data_for_named = self.__NAMED_STREAM_W_STATE.get_data_for_named()
        match data_for_named.get_enum_data_for_named():
            case EnumDataForMainVM.IS_LOADING:
                debug_print("Build: IsLoading")
            case EnumDataForMainVM.EXCEPTION:
                debug_print("Build: Exception(" + data_for_named.exception_controller.get_key_parameter_exception() + ")")
            case EnumDataForMainVM.SUCCESS:
                debug_print("Build: Success(" + data_for_named.ip_address.to_string() + ")")

    def __listen_stream_data_w_named_w_callback(self, _: DataForMainVM) -> None:
        self.__build()
            
    async def __first_request(self) -> str:
        get_ip_address_parameter_http_service = await self.__IP_ADDRESS_REPOSITORY.get_ip_address_parameter_http_service()
        if get_ip_address_parameter_http_service.EXCEPTION_CONTROLLER.is_where_not_equals_null_parameter_exception():
            return self.__first_qq_first_request_qq_get_ip_address_parameter_http_service(get_ip_address_parameter_http_service.EXCEPTION_CONTROLLER)
        self.__NAMED_STREAM_W_STATE.get_data_for_named().is_loading = False
        self.__NAMED_STREAM_W_STATE.get_data_for_named().ip_address = get_ip_address_parameter_http_service.PARAMETER.get_clone()
        return ReadyDataUtility.SUCCESS
    
    def __first_qq_first_request_qq_get_ip_address_parameter_http_service(self, exception_controller: ExceptionController) -> str:
        self.__NAMED_STREAM_W_STATE.get_data_for_named().is_loading = False
        self.__NAMED_STREAM_W_STATE.get_data_for_named().exception_controller = exception_controller
        return exception_controller.get_key_parameter_exception()

async def main() -> None:
    main_vm = MainVM()
    await main_vm.init()
    main_vm.dispose()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
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