# cmake -S . -B build
# cmake --build build
# ASAN_OPTIONS="log_path=asan.log"
# build/add_tests --gtest_output="json:add_tests.json"
# build/subtract_tests --gtest_output="json:subtract_tests.json"
# build/add_tests --gtest_output="json:add_tests.json" && build/subtract_tests --gtest_output="json:subtract_tests.json"

cmake_minimum_required(VERSION 3.10)
project(hw1 LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 14)
add_library(common INTERFACE)
target_compile_options(common INTERFACE -gdwarf-4 -Wall -Wextra -Wshadow -Wpedantic -Wdouble-promotion -Wformat=2 -Wundef -Werror)
#add_link_options(-fsanitize=address)

add_executable(hw0_main src/hw0_main.c)
target_link_libraries(hw0_main PRIVATE common)
#target_include_directories(hw1 PUBLIC include)

# set(TARGETS "add" "subtract")
# foreach(TARGET IN LISTS TARGETS)
#     add_executable(${TARGET}_tests tests/src/${TARGET}_tests.cpp src/hw1.c tests/src/valgrind.cpp)
#     target_include_directories(${TARGET}_tests PUBLIC include tests/include)
#     target_link_libraries(${TARGET}_tests PRIVATE common gtest gtest_main pthread)

#     # grading targets
#     add_executable(grading_${TARGET}_tests grading/src/${TARGET}_tests.cpp src/hw1.c tests/src/valgrind.cpp)
#     target_include_directories(grading_${TARGET}_tests PUBLIC include tests/include grading/include)
#     target_link_libraries(grading_${TARGET}_tests PRIVATE common gtest gtest_main pthread)
# endforeach()

