namespace go tutorial

typedef i32 int
service MultiplicationService{
    oneway void multiply(1:string A, 2:string B, 3:int m1, 4:int n1, 5:int m2, 6:int n2),
}
