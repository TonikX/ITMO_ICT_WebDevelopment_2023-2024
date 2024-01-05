import axios from "axios"


class HttpClient {
  get(
    url,
    params
  ) {
    return new Promise((resolve, reject) => {
      axios.get(url, {params: params}).then(res => {
        resolve(res.data)
      }).catch(e => {
        reject(e) // todo errors return
      })
    })
  }

  post(
    url,
    data
  ) {
    return new Promise((resolve, reject) => {
      axios.post(url, data).then(res => {
        resolve(res.data)
      }).catch(e => {
        reject(e) // todo errors return
      })
    })
  }

}


export default new HttpClient()