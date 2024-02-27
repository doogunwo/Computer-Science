# 컴파일러 지정
CC = g++


# 소스 파일 목록
SRCS = m1_test.cpp device_test.cpp ../common/utils.cpp ../common/nvmeprint.cpp

# 소스 파일을 기반으로한 객체 파일 목록
OBJS = $(SRCS:.cpp=.o)

# 빌드할 실행 파일 이름
EXEC = ../../bin/m1-testing

# 실행 파일 빌드 규칙
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ -lnvme -g

# 각 소스 파일을 컴파일하여 객체 파일 생성 규칙
%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

# 실행 파일 및 객체 파일 삭제 규칙
clean:
	rm -f $(EXEC) $(OBJS)
