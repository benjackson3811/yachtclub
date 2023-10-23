import React from 'react';
import {Navbar, Container, Nav } from "react-bootstrap";
import logo from '../assets/yacht_club_logo.png';
import styles from '../styles/NavBar.module.css';
import { NavLink } from "react-router-dom";
import { useCurrentUser, useSetCurrentUser } from '../contexts/CurrentUserContext';
import axios from 'axios';
import Avatar from './Avatar';

const NavBar = () => {
  const currentUser = useCurrentUser();
  const setCurrentUser = useSetCurrentUser();

const handleSignOut = async () => {
  try {
    await axios.post("dj-rest-auth/logout/");
    setCurrentUser(null);
  } catch (err) {
    console.log(err);
  }
};

  const addTripIcon = (
    <NavLink 
    className={styles.NavLink} 
    activeClassName={styles.Active} 
    to="/trips/create">
      <i class="fa-solid fa-sailboat"></i>Add trip
  </NavLink>
  )

  const loggedInIcons = (
    <>
      <NavLink
        className={styles.NavLink}
        activeClassName={styles.Active}
        to="/feed"
      >
      <i className="fas fa-stream"></i>Feed
    </NavLink>
    <NavLink
      className={styles.NavLink}
      activeClassName={styles.Active}
      to="/liked"
    >
      <i className="fas fa-heart"></i>Liked
    </NavLink>
    <NavLink className={styles.NavLink} to="/" onClick={handleSignOut}>
      <i className="fas fa-sign-out-alt"></i>Sign out
    </NavLink>
    <NavLink
      className={styles.NavLink}
      to={`/profiles/${currentUser?.profile_id}`}
    >
      <Avatar src={currentUser?.avatars} text="Profile" height={40} />
    </NavLink>
  </>
);
  const loggedOutIcons =  (
    <>
      <NavLink 
        className={styles.NavLink} 
        activeClassName={styles.Active} 
        to="/signin">

          <i className="fas fa-sign-in-alt"></i>Sign in
      </NavLink>
      <NavLink
        className={styles.NavLink} 
        activeClassName={styles.Active} 
        to="/signup"
        >
        <i className="fa-solid fa-person-circle-plus"></i>Sign up
      </NavLink>
      </>
    );

  return (
    <Navbar className={styles.NavBar} expand="md" fixed="top">
      <Container>
        <NavLink to="/">
        <Navbar.Brand>
          <img src={logo} alt='logo' height="45" />
          </Navbar.Brand>
          </NavLink>
          {currentUser && addTripIcon}
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto text-left">
            <NavLink
            exact
            className={styles.NavLink} 
            activeClassName={styles.Active} 
            to ="/">
            <i className="fa-solid fa-house-chimney"></i>Home
            </NavLink>
            {currentUser ? loggedInIcons : loggedOutIcons}
          </Nav>
        </Navbar.Collapse>
    </Container>
  </Navbar>
  );
};

export default NavBar