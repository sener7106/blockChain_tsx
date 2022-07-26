// call Signatures
// Generic, polymorphism, Overloading

/* overloading은 매우 중요합니다. */
// Polymorphism(다형성)
// concreteType : boolean, unknown, string
// genericType .. placeholder 같은 것
// <T> any 형식보다 더 안정적임

type SuperPrint = {
  <TypePlaceholder>(arr: TypePlaceholder[]): TypePlaceholder
}

const a = superPrint([1, 2, 3, 4])

function superPrint<V>(a: V[]) {
  return a[0]
}

type Player<E> = {
  name: string
  extraInfo: E
}

type NicoExtra = {
  favFood: string
}
type NicoPlayer = Player<NicoExtra>

const nicos: NicoPlayer = {
  name: 'nico',
  extraInfo: 'potato',
}
