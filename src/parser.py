import re
from typing import Optional

LOG_PATTERN = re.compile(
    r'(\S+)'              #1 ip 
    r'\s+-\s+-'                
    r'\s+\[([^\]]+)\]'        #2  time
    r'\s+"(\S+)'          #3 method
    r'\s+(\S+)'           #4 path
    r'\s+\S+'        
    r'\s+(\d+)'             #5 state code 
    r'\s+(\d+)'           #6 return byte
)

def parse_line(line: str) -> Optional[dict]:
    match = LOG_PATTERN.search(line)
    if not match:
        return None
    
    return{
        "ip" : match.group(1),
        "time" : match.group(2),
        "method" : match.group(3),
        "path" : match.group(4),
        "status" : int(match.group(5)),
        "size" : int(match.group(6)),
    }
        

def parse_file(filepath: str) -> list[dict]:
    result = []
    with open(filepath , "r" , encoding="utf-8") as f:
        for line in f :
            line = line.strip()
            if not line:
                continue
            parsed = parse_line(line)
            if parsed:
                result.append(parsed)
    return result
