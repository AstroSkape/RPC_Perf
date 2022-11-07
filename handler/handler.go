package handler

import (
	"context"
	"fmt"
	"thrift_go/gen-go/tutorial"
)

type Handler struct{}

func NewHandler() *Handler {
	return &Handler{}
}

func (p *Handler) Multiply(ctx context.Context, num1 tutorial.Int, num2 tutorial.Int) (val tutorial.Int, err error) {
	fmt.Print("multiply(", num1, ",", num2, ")\n")
	return num1 * num2, nil
}
