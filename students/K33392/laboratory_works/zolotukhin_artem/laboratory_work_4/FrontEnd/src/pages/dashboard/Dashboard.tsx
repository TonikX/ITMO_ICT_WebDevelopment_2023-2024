import { useSelector } from 'react-redux'

const Dashboard = () => {
  const { userInfo } = useSelector((state) => state.auth)
  console.log('userInfo', userInfo)

  return (
    <div>
      <h1>
        Welcome,{' '}
        {userInfo.first_name
          ? userInfo.first_name
          : 'you need to log in into your account'}
      </h1>
    </div>
  )
}

export default Dashboard
