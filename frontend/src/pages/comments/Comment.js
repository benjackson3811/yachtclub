import React from "react";
import { Media } from "react-bootstrap";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import styles from "../../styles/Comment.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { MoreDropdown } from "../../components/MoreDropdown";
import { axiosRes } from "../../api/axiosDefaults";

const Comment = (props) => {
  const {
    profile_id,
    profile_avatar,
    user,
    updated_at,
    content,
    id,
    setTrip,
    setComments,
 } = props;

  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;

  const handleDelete = async () => {
    try {
      await axiosRes.delete(`/comments/${id}/`);
      setTrip((prevTrip) => ({
        results: [
          {
            ...prevTrip.results[0],
            comments_count: prevTrip.results[0].comments_count - 1,
          },
        ],
      }));

      setComments((prevComments) => ({
        ...prevComments,
        results: prevComments.results.filter((comment) => comment.id !== id),
      }));
    } catch (err) {}
  };

  return (
    <div>
      <hr />
      <Media>
        <Link to={`/profiles/${profile_id}`}>
          <Avatar src={profile_avatar} />
        </Link>
        <Media.Body className="align-self-center ml-2">
          <span className={styles.User}>{user}</span>
          <span className={styles.Date}>{updated_at}</span>
          <p>{content}</p>
        </Media.Body>
        {is_user && (
            <MoreDropdown handleEdit={() => {}} handleDelete={handleDelete}/>
        )}
      </Media>
    </div>
  );
};

export default Comment;