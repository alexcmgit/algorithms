<p><a href="https://www.beecrowd.com.br/repository/UOJ_2611_en.html">beecrowd.com.br/repository/UOJ_2611_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2611</span>
                                    <h1>Action Movies</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>A video store contractor hired her services to catalog her movies. They need you to select the code and the name of the movies whose description of the genre is 'Action'.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>movies</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>id_genres (FK)</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>genres</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>description</td>
                              <td>varchar</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>movies</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>id_genres</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Batman</td>
                      <td>3</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>The Battle of the Dark River</td>
                      <td>3</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>White Duck</td>
                      <td>1</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Breaking Barriers</td>
                      <td>4</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>The Two Hours</td>
                      <td>2</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>genres</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>description</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Animation</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Horror</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Action</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Drama</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Comedy</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>id</strong></td>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>1</td>
          <td>Batman</td>
        </tr>
        <tr>
          <td>2</td>
          <td>The Battle of the Dark River</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>