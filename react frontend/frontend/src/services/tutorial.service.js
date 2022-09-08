import http from "../http-common";
class TutorialDataService {
  getAll() {
    return http.get("/Tutorial");
  }
  get(id) {
    return http.get(`/Tutorial/${id}`);
  }
  create(data) {
    return http.post("/Tutorial", data);
  }
  update(id, data) {
    return http.put(`/Tutorial/${id}`, data);
  }
  delete(id) {
    return http.delete(`/Tutorial/${id}`);
  }
  deleteAll() {
    return http.delete(`/Tutorial`);
  }
  findByTitle(title) {
    return http.get(`/Tutorials?title=${title}`);
  }
}
export default new TutorialDataService();