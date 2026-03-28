#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}🚀 파이썬 프로그램을 실행합니다...${NC}"
echo "------------------------------------------"

python3 main.py
EXIT_CODE=$?

echo -e "------------------------------------------"
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ 실행 성공 (Exit Code: 0)${NC}"
else
    echo -e "${RED}❌ 실행 중 에러 발생 (Exit Code: $EXIT_CODE)${NC}"
fi

exit $EXIT_CODE
