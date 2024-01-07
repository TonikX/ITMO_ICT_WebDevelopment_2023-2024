import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {
  addAnimal,
  deleteAnimal,
  getAnimals,
  updateAnimal,
} from '../../features/animals/animalSlice'

type AnimalData = {
  num: string
  name: string
  age: number
  sex: 'm' | 'f'
  diet: string
  birthdate: string
  owner: string
  previous_owner: string
  in_lease: boolean
  where_is_now: string
  since: string
}

const AnimalsPage = () => {
  const [newAnimalData, setNewAnimalData] = useState<AnimalData>({
    num: '',
    name: '',
    age: 0,
    sex: 'm',
    diet: '',
    birthdate: '', // Add a state for birthdate
    owner: '', // Add a state for owner
    previous_owner: '', // Add a state for previous owner
    in_lease: false, // Add a state for in_lease
    where_is_now: '', // Add a state for where_is_now
    since: '', // Add a state for since
  })
  const [selectedAnimal, setSelectedAnimal] = useState<AnimalData | null>(null)
  const { animals, isLoading, isError, message } = useSelector(
    (state: any) => state.animals
  )
  const dispatch = useDispatch()
  const { user } = useSelector((state) => state.auth)

  useEffect(() => {
    if (user && user.access) {
      dispatch(getAnimals(user.access))
    }
  }, [dispatch, user])

  const handleAddAnimal = () => {
    if (user && user.access) {
      dispatch(addAnimal({ data: newAnimalData, token: user.access }))
    }
    setNewAnimalData({ num: '', name: '', age: 0, sex: 'm', diet: '' })
  }

  const handleEditClick = (animal: AnimalData) => {
    setSelectedAnimal(animal)
    setNewAnimalData(animal)
  }

  const handleUpdateAnimal = () => {
    if (selectedAnimal && user && user.access) {
      dispatch(
        updateAnimal({
          id: selectedAnimal.id,
          data: newAnimalData,
          token: user.access,
        })
      )

      setSelectedAnimal(null)
    }
  }

  const handleDeleteAnimal = (id: string) => {
    if (user && user.access) {
      dispatch(deleteAnimal({ id: id, token: user.access }))
    }
  }

  if (isLoading) return <p>Loading animals...</p>
  if (isError) return <p>Error: {message}</p>

  if (!Array.isArray(animals)) return <p>Error: Animals data is not an array</p>

  return (
    <div>
      <h1>Animals</h1>
      {animals.map((animal: AnimalData) => (
        <div key={animal.id}>
          <h2>{animal.name}</h2>
          <p>Number: {animal.num}</p>
          {/* More details... */}
          <button onClick={() => handleEditClick(animal)}>Edit</button>
          <button onClick={() => handleDeleteAnimal(animal.id)}>Delete</button>
        </div>
      ))}
      <div>
        {selectedAnimal ? <h2>Edit Animal</h2> : <h2>Add New Animal</h2>}
        {/* Form for adding or editing an animal */}
        <input
          type='text'
          placeholder='Number'
          value={newAnimalData.num}
          onChange={(e) =>
            setNewAnimalData({ ...newAnimalData, num: e.target.value })
          }
        />
        {/* I need to add more inputs later, but that works! */}
        {selectedAnimal ? (
          <button onClick={handleUpdateAnimal}>Update Animal</button>
        ) : (
          <button onClick={handleAddAnimal}>Add Animal</button>
        )}
      </div>
    </div>
  )
}

export default AnimalsPage
