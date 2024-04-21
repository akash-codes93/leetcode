/**
https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=daily-question&envId=2024-04-21
**/

package main

import (
	"container/list"
	"fmt"
)

func validPath(n int, edges [][]int, source int, destination int) bool {

	if source == destination {
		return true
	}
	egdeMap := map[int][]int{}

	for _, edge := range edges {
		egdeMap[edge[0]] = append(egdeMap[edge[0]], edge[1])
		egdeMap[edge[1]] = append(egdeMap[edge[1]], edge[0])
	}

	queue := list.New()

	for _, edge := range egdeMap[source] {
		queue.PushBack(edge)
	}

	visited := map[int]bool{}
	var element *list.Element

	for queue.Len() > 0 {

		element = queue.Front()     // getting a generic element from list of type list.Element
		edge := element.Value.(int) // using type assertion
		queue.Remove(element)

		if edge == destination {
			return true
		}

		for _, nextEdge := range egdeMap[edge] {
			if _, ok := visited[nextEdge]; !ok {
				visited[nextEdge] = true
				queue.PushBack(nextEdge)
			}
		}
	}
	return false
}

func main() {
	fmt.Println(validPath(3, [][]int{{0, 1}, {1, 2}, {2, 0}}, 0, 2))
	// fmt.Println(validPath(6, [][]int{{0, 1}, {0, 2}, {3, 5}, {5, 4}, {4, 3}}, 0, 5))
}
