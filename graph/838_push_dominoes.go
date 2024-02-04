package main

import "container/list"

type DominoState struct {
	time  int
	state byte
}

type DominoPush struct {
	time  int
	index int
	state byte
}

func pushDominoes(dominoes string) string {

	dominoStates := make([]*DominoState, len(dominoes))

	// creating current state of dominoes
	for i := 0; i < len(dominoes); i++ {
		dominoStates[i] = &DominoState{time: 0, state: dominoes[i]}
	}

	queue := list.New()

	// creating a push of dominoes
	for i := 0; i < len(dominoes); i++ {
		if dominoes[i] != '.' {
			queue.PushBack(
				&DominoPush{
					time:  0,
					state: dominoes[i],
					index: i,
				},
			)
		}
	}

	var push *DominoPush
	var element *list.Element
	var newIndex int
	var newTime int
	var dominoState *DominoState

	// calculating push for other dominoes
	for queue.Len() > 0 {

		element = queue.Front()            // element
		push = element.Value.(*DominoPush) // type assertion
		queue.Remove(element)

		if push.state == 'R' {
			newIndex = push.index + 1
			newTime = push.time + 1
			if newIndex >= len(dominoes) {
				continue
			}

			dominoState = dominoStates[newIndex]
			if dominoState.time > newTime {
				continue
			} else {
				if dominoState.state == '.' {
					dominoState.state = 'R'
					queue.PushBack(&DominoPush{
						time:  newTime,
						state: dominoState.state,
						index: newIndex,
					})
				} else if dominoState.state == 'L' {
					dominoState.state = '.'
				}
			}
		} else if push.state == 'L' {

		}

	}
	var ret = make([]byte, len(dominoes))

	for i := 0; i < len(dominoes); i++ {
		ret[i] = dominoStates[i].state
	}
	return string(ret)

}
