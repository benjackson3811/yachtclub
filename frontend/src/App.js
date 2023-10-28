import styles from "./App.module.css";
import NavBar from "./components/NavBar";
import Container from "react-bootstrap/Container";
import { Route, Switch } from "react-router-dom";
import './api/axiosDefaults'
import SignUpForm from "./pages/auth/SignUpForm";
import SignInForm from "./pages/auth/SignInForm";
import TripCreateForm from "./pages/trips/TripCreateForm";
import TripPage from "./pages/trips/TripPage";
import TripsPage from "./pages/trips/TripsPage";
import { useCurrentUser } from "./contexts/CurrentUserContext";

function App() {
  const currentUser = useCurrentUser()
  const profile_id = currentUser?.profile.id || "";

  return (
    <div className={styles.App}>
      <NavBar />
      <Container className={styles.Main}>
        <Switch>
          <Route exact path="/" render={() => <TripsPage message="No Results found. Adjust the search keyword."/>} />
          <Route exact path="/feed" render={() => <TripsPage message="No Results found. Adjust the search keyword or follow a user."/>} 
          filter={`user__followed__user=${profile_id}&`}/>
          <Route exact path="/liked" render={() => <TripsPage message="No Results found. Adjust the search keyword or like a post."/>} 
          filter={`likes__user=${profile_id}&ordering=-likes__created_at&`}/>
          <Route exact path="/signin" render={() => <SignInForm />} />
          <Route exact path="/signup" render={() => <SignUpForm />} />
          <Route exact path="/trips/create" render={() => <TripCreateForm />} />
          <Route exact path="/trips/:id" render={()=> <TripPage />} />
          <Route render={() => <p>Page not found!</p>} />
        </Switch>
      </Container>
    </div>
  );
}

export default App;