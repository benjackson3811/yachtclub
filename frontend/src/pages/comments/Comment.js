import React, { useState } from "react";
import { Media } from "react-bootstrap";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { MoreDropdown } from "../../components/MoreDropdown";
import CommentEditForm from "./CommentEditForm";
import styles from "../../styles/Comment.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
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

  const [showEditForm, setShowEditForm] = useState(false);
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
    <>
      <hr />
      <Media>
        <Link to={`/profiles/${profile_id}`}>
          <Avatar src={profile_avatar} />
        </Link>
        <Media.Body className="align-self-center ml-2">
          <span className={styles.User}>{user}</span>
          <span className={styles.Date}>{updated_at}</span>
          {showEditForm ? (
            <CommentEditForm
                id={id}
                profile_id={profile_id}
                content={content}
                profileAvatar={profile_avatar}
                setComments={setComments}
                setShowEditForm={setShowEditForm}
              />
          ) : (
            <p>{content}</p>
          )}
        </Media.Body>
        {is_user && !showEditForm && (
          <MoreDropdown
            handleEdit={() => setShowEditForm(true)}
            handleDelete={handleDelete}
          />
        )}
      </Media>
    </>
  );
};

export default Comment;