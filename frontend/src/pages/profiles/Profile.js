import React from "react";
import styles from "../../styles/Profile.module.css";
import btnStyles from "../../styles/Button.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import Avatar from "../../components/Avatar";
import { Link } from "react-router-dom/cjs/react-router-dom";
import { Button } from "react-bootstrap";
import { useSetProfileData } from "../../contexts/ProfileDataContext";

const Profile = (props) => {
    const { profile, mobile, avatarSize = 35 } = props;
    const { id, following_id, avatar, user } = profile;

    const currentUser = useCurrentUser();
    const is_user = currentUser?.username === user;

    const {handleFollow } = useSetProfileData();

    return (
        <div
          className={`my-3 d-flex align-items-center ${mobile && "flex-column"}`}
        >
          <div>
            <Link className="align-self-center" to={`/profiles/${id}`}>
              <Avatar src={avatar} height={avatarSize} />
            </Link>
          </div>
          <div className={`mx-2 ${styles.WordBreak}`}>
            <strong>{user}</strong>
          </div>
          <div className={`text-right ${!mobile && "ml-auto"}`}>
            {!mobile &&
              currentUser &&
              !is_user &&
              (following_id ? (
                <Button
                  className={`${btnStyles.Button} ${btnStyles.BlackOutline}`}
                  onClick={() => {}}
                >
                  unfollow
                </Button>
              ) : (
                <Button
                  className={`${btnStyles.Button} ${btnStyles.Black}`}
                  onClick={() => handleFollow(profile)}
                >
                  follow
                </Button>
              ))}
          </div>
        </div>
      );
    };

export default Profile