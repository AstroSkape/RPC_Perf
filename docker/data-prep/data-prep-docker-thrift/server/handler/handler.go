package handler

import (
	"context"
	"fmt"
)

type Handler struct{}

func NewHandler() *Handler {
	return &Handler{}
}

func (p *Handler) Multiply(ctx context.Context, A string) (val string, err error) {
	fmt.Println("In multiply...")
	/*M1 := decode(A)
	M2 := decode(B)

	arr := make([][]int, int(m1))
	for i := 0; i < int(m1); i++ {
		arr[i] = make([]int, int(n2))
	}

	for i := 0; i < int(m1); i++ {
		for j := 0; j < int(n2); j++ {
			arr[i][j] = 0
			for k := 0; k < int(n1); k++ {
				arr[i][j] += (M1[i][k] * M2[k][j])
			}
		}
	}

	return encode(arr, int(m1), int(n2)), nil*/

	return "done", nil
}
