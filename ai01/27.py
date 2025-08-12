def http_errors(status: int):
	match status:
		case 400:
			return '客户端错误'
		case 401:
			return '鉴权失败'
		case 500:
			return '服务端错误'
		case x:
			return '未知错误'

print(http_errors(401))