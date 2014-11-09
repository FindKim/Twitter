all: sequential

sequential: sequential.cpp
	g++ sequential.cpp -o sequential

clean:
	rm -f *~ sequential
