import instance from "@/domain/instance";

class LibraryApi {
  constructor(instance) {
    this.API = instance
  }

  register = async (signUpForm) => {
    await this.API.post('/auth/users/', signUpForm, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }

  login = async (username, password) => {
    return await this.API.post('/auth/token/login/',
      {
        password: password,
        username: username
      })
  }

  getTakingBooks = async () => {
    return await this.API.get('/library/taking_book/list')
  }

  deleteTakingBooks = async (id) => {
    await this.API.delete('/library/taking_book/delete/' + id)
  }

  sendTakingBook = async (instanceBook) => {
    return await this.API.post('/library/taking_book/give', instanceBook)
  }

  getAllBooks = async () => {
    return await this.API.get('/library/books/list/')
  }

  getReadersList = async () => {
    return await this.API.get('/library/readers/list/')
  }

  getBook = async (id) => {
    return await this.API.get('/library/books/' + id)
  }

  getUser = async () => {
    return await this.API.get('/auth/users/me/', {
        headers: {
          Authorization: `Token ${localStorage.auth_token}`,
        }
      }
    )
  }

  changeUserData = async (userData) => {
    await this.API.patch('/auth/users/me/', userData)
  }
}

const libraryApi = new LibraryApi(instance)
export default libraryApi
