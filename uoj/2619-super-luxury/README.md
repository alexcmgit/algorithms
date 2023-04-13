<p><a href="https://www.beecrowd.com.br/repository/UOJ_2619_en.html">beecrowd.com.br/repository/UOJ_2619_en.html</a></p><hr>
                                          <div>
                                            <span>URI Online <strong>SQL</strong> | 2619 </span>
                                            <h1>Super Luxury</h1>
                                            <div>
                                              <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                            </div>
                                            <strong>Timelimit: 1</strong>
                                          </div>
                                          <div>
                                          <div>
                                            <p>Our company is looking to make a new contract for the supply of new super luxury products, and for this we need some data of our products.</p>
                                            <p>Your job is to display the name of the products, the name of the providers and the price, for the products whose price is greater than 1000 and its category is' Super Luxury.</p>
                                          </div>
                                          <div>
                                          <h2>Schema</h2>
                                          <div>
                                          <table>
                                          <caption>products</caption>
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
                                          <td>character varying (255)</td>
                                        </tr>
                                        <tr>
                                          <td>amount</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>price</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>id_providers (FK)</td>
                                          <td>numeric</td>
                                        </tr>
                                        <tr>
                                          <td>id_categories (FK)</td>
                                          <td>numeric</td>
                                        </tr>
                                      </tbody></table>
                                      <table>
                                      <caption>providers</caption>
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
                                      <td>character varying (255)</td>
                                    </tr>
                                    <tr>
                                      <td>street</td>
                                      <td>character varying (255)</td>
                                    </tr>
                                    <tr>
                                      <td>city</td>
                                      <td>character varying (255)</td>
                                    </tr>
                                    <tr>
                                      <td>state</td>
                                      <td>char (2)</td>
                                    </tr>
                                  </tbody></table>
                                  <table>
                                  <caption>categories</caption>
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
                                  <td>character varying (255)</td>
                                </tr>
                              </tbody></table>
                            </div>
                          </div>
                          <div>
                          <h2>Tables</h2>
                          <div>
                          <table>
                          <caption>products</caption>
                          <tbody><tr>
                          <td><strong>id</strong></td>
                          <td><strong>name</strong></td>
                          <td><strong>amount</strong></td>
                          <td><strong>price</strong></td>
                          <td><strong>id_providers</strong></td>
                          <td><strong>id_categories</strong></td>
                        </tr>
                        <tr>
                          <td>1</td>
                          <td>Blue Chair</td>
                          <td>30</td>
                          <td>300.00</td>
                          <td>5</td>
                          <td>5</td>
                        </tr>
                        <tr>
                          <td>2</td>
                          <td>Red Chair</td>
                          <td>50</td>
                          <td>2150.00</td>
                          <td>2</td>
                          <td>1</td>
                        </tr>
                        <tr>
                          <td>3</td>
                          <td>Disney Wardrobe</td>
                          <td>400</td>
                          <td>829.50</td>
                          <td>4</td>
                          <td>1</td>
                        </tr>
                        <tr>
                          <td>4</td>
                          <td>Blue Toaster</td>
                          <td>20</td>
                          <td>9.90</td>
                          <td>3</td>
                          <td>1</td>
                        </tr>
                        <tr>
                          <td>5</td>
                          <td>TV</td>
                          <td>30</td>
                          <td>3000.25</td>
                          <td>2</td>
                          <td>2</td>
                        </tr>
                      </tbody></table>
                      <table>
                      <caption>providers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                      <td><strong>state</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Ajax SA</td>
                      <td>Rua Presidente Castelo Branco</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Sansul SA</td>
                      <td>Av Brasil</td>
                      <td>Rio de Janeiro</td>
                      <td>RJ</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>South Chairs</td>
                      <td>Rua do Moinho</td>
                      <td>Santa Maria</td>
                      <td>RS</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Elon Electro</td>
                      <td>Rua Apolo</td>
                      <td>São Paulo</td>
                      <td>SP</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Mike electro</td>
                      <td>Rua Pedro da Cunha</td>
                      <td>Curitiba</td>
                      <td>PR</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>categories</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Super Luxury</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Imported</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Tech</td>
                </tr>
                <tr>
                  <td> 4</td>
                  <td>Vintage</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Supreme</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>name</strong></td>
          <td><strong>price</strong></td>
        </tr>
        <tr>
          <td>Red Chair</td>
          <td>Sansul SA</td>
          <td>2150.00</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>