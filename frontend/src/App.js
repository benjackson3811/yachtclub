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
import TripEditForm from "./pages/trips/TripEditForm";
import ProfilePage from "./pages/profiles/ProfilePage";
import UsernameForm from "./pages/profiles/UsernameForm";
import UserPasswordForm from "./pages/profiles/UserPasswordForm";
import ProfileEditForm from "./pages/profiles/ProfileEditForm";

function App() {
  const currentUser = useCurrentUser();
  const profile_id = currentUser?.profile_id || "";

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
          <Route exact path="/trips/:id/edit" render={() => <TripEditForm />} />
          <Route exact path="/profiles/:id" render={() => <ProfilePage />} />
          <Route exact path="/profiles/:id/edit/username" render={() => <UsernameForm />} />
          <Route exact path="/profiles/:id/edit/password" render={() => <UserPasswordForm />} />
          <Route exact path="/profiles/:id/edit" render={() => <ProfileEditForm />} />
          <Route render={() => <p>Page not found!</p>} />
        </Switch>
      </Container>
    </div>
  );
}

export default App;