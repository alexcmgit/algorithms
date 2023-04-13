<p><a href="https://www.beecrowd.com.br/repository/UOJ_2613_en.html">beecrowd.com.br/repository/UOJ_2613_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2613 </span>
                                    <h1>Cheap Movies</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>In the past the studio has made an event where several movies were on sale, we want to know what movies these were.</p>
                                    <p>Your job to help us is to select the ID and name of movies whose price is less than 2.00.</p>
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
                                  <td>id_prices (FK)</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>prices</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>categorie</td>
                              <td>varchar</td>
                            </tr>
                            <tr>
                              <td>value</td>
                              <td>numeric</td>
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
                      <td><strong>id_prices</strong></td>
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
                      <td>5</td>
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
                  <caption>prices</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>categorie</strong></td>
                  <td><strong>value</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Releases</td>
                  <td>3.50</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Bronze Seal</td>
                  <td>2.00</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Silver Seal</td>
                  <td>2.50</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Gold Seal</td>
                  <td>3.00</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Promotion</td>
                  <td>1.50</td>
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
          <td>3</td>
          <td>White Duck</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>