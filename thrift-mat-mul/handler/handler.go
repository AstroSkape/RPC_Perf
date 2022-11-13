package handler

import (
	"SSP_Project/thrift-mat-mul/gen-go/tutorial"
	"context"
	"fmt"
	"strconv"
	"strings"
)

type Handler struct{}

func NewHandler() *Handler {
	return &Handler{}
}

func decode(s string) [][]int {
	rows := strings.Split(s, ";");
	numRows := len(rows);
	numRows--;
	numCols := len(strings.Split(rows[0], ","));
	arr := make([][]int, numRows);
	for i := 0; i<numRows; i++ {
		arr[i] = make([]int, numCols);
	}
	m := 0;
	n := 0;
	for i := 0; i<numRows; i++ {
		row := rows[i];
		eles := strings.Split(row, ",");
		for j := 0; j<numCols; j++ {
			//fmt.Println("ELE = ", eles[j]);
			arr[m][n], _ = strconv.Atoi(eles[j]);
			n++;
		}
		n = 0;
		m++;
	}
	
	return arr;
}

func encode(arr [][]int, m int, n int) string {
	res := "";
	for i := 0; i<m; i++ {
		for j := 0; j<n; j++ {
			res = res + strconv.Itoa(arr[i][j]);
			if(j == n-1) {
				res = res + ";";
			} else {
				res = res + ",";
			}
		}
	}
	
	return res;
	
}

func (p *Handler) Multiply(ctx context.Context, A string, B string, m1 tutorial.Int, n1 tutorial.Int, m2 tutorial.Int, n2 tutorial.Int) (val string, err error) {
	fmt.Println("In multiply...");
	M1 := decode(A);
	M2 := decode(B);
	
	arr := make([][]int, int(m1));
	for i := 0; i<int(m1); i++ {
		arr[i] = make([]int, int(n2));
	}
	
	for i:=0; i<int(m1); i++ {
		for j := 0; j<int(n2); j++ {
			arr[i][j] = 0;
			for k := 0; k<int(n1); k++ {
				arr[i][j] += (M1[i][k]*M2[k][j]);
			}
		}
	}
	
	return encode(arr, int(m1), int(n2)), nil
}
