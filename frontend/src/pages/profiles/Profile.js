import React from "react";
import styles from "../../styles/Profile.module.css";
import btnStyles from "../../styles/Button.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";

const Profile = () => {
    const { profile, mobile, imageSize = 55 } = props;
    const { id, following_id, image, user } = profile;

    const currentUser = useCurrentUser();
    const is_user = currentUser?.username === user;
  return (
    <div></div>
  )
}

export default Profile